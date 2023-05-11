
from rest_framework.views import APIView
from chat.models import Room, RoomJoin, Message
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from collections import Counter


class RoomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 유저가 속해있는 채팅룸 조회기능
        user_chat_room = RoomJoin.objects.filter(user_id=request.user.id)
        room_info = {}
        for chat_room in user_chat_room:
            room_id = chat_room.room_id.id
            chat_user_list = RoomJoin.objects.filter(room_id=room_id)

            room_user_list = []
            for user_list in chat_user_list:
                username = user_list.user_id.email
                room_user_list.append(username)

            room_info[room_id] = room_user_list
        if room_info == {}:
            room_info = None
        return Response(room_info, status=status.HTTP_200_OK)

    def post(self, request):
        # 게시글 작성자와 1:1 채팅방이 존재한다면 해당 채팅방 id를 전해준다.
        # 존재하지 않는다면 채팅방을 새로 개설하고 id를 전해준다

        user1 = User.objects.get(id=request.user.id)
        user2 = User.objects.get(id=request.data.get('author'))
        find_room_q = RoomJoin.objects.filter(user_id__in=[user1.id, user2.id])
        
        find_room_list = []
        for find_room in find_room_q:
            find_room_list.append(find_room.room_id)

        result = Counter(find_room_list)
        for key, value in result.items():
            if value >= 2:
                return Response(key.id, status=status.HTTP_200_OK)

        room = Room.objects.create()
        RoomJoin.objects.create(user_id=user1, room_id=room)
        RoomJoin.objects.create(user_id=user2, room_id=room)

        return Response(room.id, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            room = Room.objects.get(id=request.data.get('room_id'))
            room.delete()
            return Response(status=status.HTTP_200_OK)

        except:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)


class ChatRoom(APIView):

    def get(self, request):
        # 현제 로그인한 유저가 특정 채팅방에 대한 정보를 가져올때 사용.
        room_id = request.data.get('room_id', None)
        try:
            check_room = RoomJoin.objects.get(user_id=request.user.id, room_id=room_id)
            message = Message.objects.filter(room_id=room_id)
            # 프로필이미지 출력하려면 추가.

            return Response(message, status=status.HTTP_200_OK)

        except:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

