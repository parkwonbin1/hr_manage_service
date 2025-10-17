from django.db import models
from django.urls import reverse


class Employee(models.Model):
    """직원 모델"""
    
    # 직급 선택지
    POSITION_CHOICES = [
        ('intern', '인턴'),
        ('junior', '주니어'),
        ('senior', '시니어'),
        ('lead', '리드'),
        ('manager', '매니저'),
        ('director', '디렉터'),
        ('ceo', 'CEO'),
    ]
    
    # 부서 선택지
    DEPARTMENT_CHOICES = [
        ('development', '개발팀'),
        ('design', '디자인팀'),
        ('marketing', '마케팅팀'),
        ('sales', '영업팀'),
        ('hr', '인사팀'),
        ('finance', '재무팀'),
        ('management', '경영진'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='이름')
    email = models.EmailField(verbose_name='이메일', unique=True)
    phone = models.CharField(max_length=20, verbose_name='전화번호', blank=True)
    department = models.CharField(
        max_length=20, 
        choices=DEPARTMENT_CHOICES, 
        verbose_name='부서'
    )
    position = models.CharField(
        max_length=20, 
        choices=POSITION_CHOICES, 
        verbose_name='직급'
    )
    hire_date = models.DateField(verbose_name='입사일')
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=0, 
        verbose_name='급여',
        null=True, 
        blank=True
    )
    is_active = models.BooleanField(default=True, verbose_name='재직 상태')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    
    class Meta:
        verbose_name = '직원'
        verbose_name_plural = '직원들'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_department_display()})"
    
    def get_absolute_url(self):
        return reverse('employees:employee_detail', kwargs={'pk': self.pk})