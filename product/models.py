from django.db import models
from users.models import User
from django.utils import timezone


# 카테고리 모델
class ProductCategory(models.Model):
    name = models.CharField("분류", max_length=50, unique=True)
    is_used = models.BooleanField("True=사용, False=사용안함", default=True)
    """
    인기매물, 
    디지털기기, 
    생활가전, 
    가구 인테리어, 
    생활 주방, 
    유아동, 
    도서, 
    여성의류,
    여성잡화, 
    남성의류,
    남성잡화, 
    뷰티 미용, 
    스포츠 레저, 
    취미/게임 음반, 
    중고차, 
    티켓 교환권, 
    가공식품, 
    반려동물용품, 
    식물, 
    기타 중고물품, 
    삽니다, 
    부동산
    """
    def __str__(self):
        return self.name


# 상품 모델
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 내용
    title = models.CharField("제목", max_length=50)
    content = models.TextField("내용", blank=False)
    price = models.IntegerField("가격")
    is_free = models.BooleanField("무료나눔", default=False)           # True=무료나눔, False=판매
    # image = models.ImageField("사진", blank=True, upload_to='%Y/%m/')
    bargain = models.BooleanField("가격제안 여부", default=False)      # True=가격제안 가능, False=가격제안 불가
    place = models.TextField("장소", blank=True)
    category = models.ManyToManyField(ProductCategory, related_name='product')

    # 필터링 or 정렬 관련
    views = models.IntegerField("조회수", default=0)
    transaction_status = models.IntegerField("거래상태", default=0)    # 0=판매중, 1=예약중, 2=판매완료
    refreshed_at = models.DateTimeField("끌어올리기", null=True)       # 끌어올리기 할때마다 최신화, 리스트 정렬 기준으로 사용
    is_hide = models.BooleanField("숨기기", default=False)             # True=숨기기, False=보이기
    
    # 관심상품
    bookmark = models.ManyToManyField(User, related_name='bookmark_product', blank=True)
    
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    
    # 삭제시 복구가능하게?
    # is_delete = models.BooleanField("삭제요청", default=False)          # True=유저가 삭제요청했을때 삭제한걸로 취급, False=존재하는 글로 취급

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        끌어올리기 사용가능 최소시간을 지정할 수 있다.
        상품 리스트의 정렬 기준이 되기 때문에 초기값을 현재시간으로 지정해주고 끌어올리기 요청시마다 시간을 업데이트 해준다.
        """
        # 상품 등록시 정렬기준으로 쓰기위해 초기값 생성
        if not self.pk:
            self.refreshed_at = timezone.now()
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


# 상품 이미지 모델
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("이미지", upload_to='%Y/%m/', null=True, blank=True, default=None)
