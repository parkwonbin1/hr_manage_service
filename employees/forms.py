from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """직원 폼"""
    
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'department', 'position', 'hire_date', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '이름을 입력하세요'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '이메일을 입력하세요'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '전화번호를 입력하세요'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'position': forms.Select(attrs={
                'class': 'form-control'
            }),
            'hire_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '급여를 입력하세요'
            }),
        }
        labels = {
            'name': '이름',
            'email': '이메일',
            'phone': '전화번호',
            'department': '부서',
            'position': '직급',
            'hire_date': '입사일',
            'salary': '급여',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필수 필드 표시
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['department'].required = True
        self.fields['position'].required = True
        self.fields['hire_date'].required = True
