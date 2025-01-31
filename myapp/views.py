from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
# def home(request):
#     students = Student.objects.all()  # if you want to retrieve all students
#     return render(request, 'myapp/home.html', {'students': students})

class homeCV(ListView):
    model = Student
    template_name = 'myapp/home.html'
    context_object_name = 'students'


# def add(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student added successfully')
#             return redirect('home')
            
#     else:
#         form = StudentForm()
#     return render(request, 'myapp/add.html', {'form': form})

class addCV(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'myapp/add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)




# def update(request, id):
#     student = Student.objects.get(id=id)
#     form = StudentForm(request.POST or None, instance=student)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Student updated successfully')
#         return redirect('home')
        
#     return render(request, 'myapp/edit.html', {'form': form})


# Update student details
class UpdateCV(UpdateView):
    model = Student
    form_class = StudentForm
    pk_url_kwarg = 'id'
    template_name = 'myapp/edit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Student details updated successfully!")
        return super().form_valid(form)



# def delete(request, id):
#     student = Student.objects.get(id=id)
#     student.delete()
#     messages.success(request, 'Student deleted successfully')
#     return redirect('home')


# Delete a student
class DeleteCV(DeleteView):
    model = Student
    pk_url_kwarg = 'id'
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)