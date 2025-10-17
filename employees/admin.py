from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """직원 관리자 인터페이스"""
    
    list_display = ['name', 'email', 'department', 'position', 'hire_date', 'is_active']
    list_filter = ['department', 'position', 'is_active', 'hire_date']
    search_fields = ['name', 'email', 'phone']
    list_editable = ['is_active']
    ordering = ['-created_at']
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('name', 'email', 'phone')
        }),
        ('직무 정보', {
            'fields': ('department', 'position', 'hire_date', 'salary')
        }),
        ('상태 정보', {
            'fields': ('is_active',),
            'classes': ('collapse',)
        }),
        ('시스템 정보', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'readonly_fields': ('created_at', 'updated_at')
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_readonly_fields(self, request, obj=None):
        """수정 시에는 생성일시를 읽기 전용으로 설정"""
        if obj:  # 편집 모드
            return self.readonly_fields + ['created_at']
        return self.readonly_fields
    
    def save_model(self, request, obj, form, change):
        """저장 시 추가 로직"""
        super().save_model(request, obj, form, change)