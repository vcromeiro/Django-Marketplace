from django.views.generic import TemplateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from home.forms import HomeForm
# from home.models import Post, Friend
from home.models import Product

def home(request):
    products = Product.objects.all().order_by('-created')
    userproducts = Product.objects.filter(user=request.user)
    args = {'products': products, 'userproducts': userproducts}
    return render(request, 'home/home.html', args)
    
def view_product(request, pk=None):
    vproduct = Product.objects.get(pk=pk)
    args = {'vproduct': vproduct}
    return render(request, 'home/view_product.html', args)
    
def edit_product(request, pk=None):
    if request.method == 'POST':
        instance = Product.objects.get(pk=pk)
        form = HomeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('home:home')
        
    else:
        instance = Product.objects.get(pk=pk)
        data = {'name': instance.name, 'description': instance.description, 'image': instance.image,'price': instance.price}
        form = HomeForm(initial = data)
        args = {
            'instance': instance, 
            'form': form,
        }
    return render(request, 'home/edit_product.html', args)
    
class Delete_product(DeleteView):
    model = Product
    success_url = reverse_lazy('home:home')
    

class NewProduct(TemplateView):
    template_name = 'home/new_product.html'
    
    def get(self, request):
        form = HomeForm()
        
        args = {'form': form}
        return render(request, self.template_name, args)
        
    def post(self, request):
        form = HomeForm(request.POST, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            return redirect('home:home')
        
        args = {'form': form}
        return render(request, self.template_name, args)

    
"""
class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        
        args = {
            'form': form, 'posts': posts, 'users': users,
            'friends': friends
            
        }
        return render(request, self.template_name, args)
        
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')
            
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
        
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')
    
"""