from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    """직원 목록 조회"""
    search_query = request.GET.get('search', '')
    department_filter = request.GET.get('department', '')
    
    employees = Employee.objects.filter(is_active=True)
    
    # 검색 기능
    if search_query:
        employees = employees.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    
    # 부서 필터
    if department_filter:
        employees = employees.filter(department=department_filter)
    
    # 페이지네이션
    paginator = Paginator(employees, 10)  # 페이지당 10개
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'department_filter': department_filter,
        'departments': Employee.DEPARTMENT_CHOICES,
    }
    return render(request, 'employees/employee_list.html', context)


def employee_detail(request, pk):
    """직원 상세 조회"""
    employee = get_object_or_404(Employee, pk=pk)
    context = {'employee': employee}
    return render(request, 'employees/employee_detail.html', context)


def employee_create(request):
    """직원 추가"""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'{employee.name} 직원이 성공적으로 추가되었습니다.')
            return redirect('employees:employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm()
    
    context = {'form': form, 'title': '직원 추가'}
    return render(request, 'employees/employee_form.html', context)


def employee_update(request, pk):
    """직원 정보 수정"""
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'{employee.name} 직원 정보가 성공적으로 수정되었습니다.')
            return redirect('employees:employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    
    context = {'form': form, 'employee': employee, 'title': '직원 정보 수정'}
    return render(request, 'employees/employee_form.html', context)


def employee_delete(request, pk):
    """직원 삭제 (실제로는 is_active를 False로 변경)"""
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        employee.is_active = False
        employee.save()
        messages.success(request, f'{employee.name} 직원이 삭제되었습니다.')
        return redirect('employees:employee_list')
    
    context = {'employee': employee}
    return render(request, 'employees/employee_confirm_delete.html', context)