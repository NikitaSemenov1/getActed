from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .filters import *
from .models import *


def index(request):
    return render(request, "main/index.html", context={
        'index': True
    })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Неправильный логин или пароль')
    return render(request, 'registration/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def signup_page(request):
    if request.method == 'POST':
        if request.POST.get('user_type') == 'actor':
            form = CreateActorForm(request.POST)
        else:
            form = CreateEmployerForm(request.POST)

        if form.is_valid():
            messages.success(request, 'You have successfully signed up')
            form.save()
            return redirect('signup')
        else:
            messages.error(request, form.errors)

    return render(request, "registration/signup.html")


@login_required(login_url='login')
def actor_profile_page(request, actor_id):
    if hasattr(request.user, 'employer'):
        return render(request, "main/actor_profile.html", context={
            'actor': Actor.objects.get(id=actor_id)
        })
    elif request.user.actor.id != actor_id:
        return redirect('index')

    if not hasattr(request.user, 'actor'):

        return redirect('index')

    actor = request.user.actor

    if request.method == 'POST':
        if request.POST.get('Accept') is not None:
            r2a = RequestRoleToActor.objects.get(id=request.POST['Accept'])
            r2a.accept()
            r2a.save()
        elif request.POST.get('Deny') is not None:
            r2a = RequestRoleToActor.objects.get(id=request.POST['Deny'])
            r2a.deny()
            r2a.save()
        else:
            form = ActorModelForm(request.POST, instance=actor)

            if form.is_valid():
                form.save()
                messages.success(request, "Saved")
            else:
                messages.error(request, form.errors)
    form = ActorModelForm(instance=actor)
    if not hasattr(request.user, 'employer'):
        actor2role = RequestActorToRole.objects.filter(actor=request.user.actor).order_by("-id")
        role2actor = RequestRoleToActor.objects.filter(actor=request.user.actor,
                                                       is_denied=False, is_accepted=False).order_by("-id")
    return render(request, "main/actor_profile.html", context={
        'form': form,
        'actor2role': actor2role,
        'role2actor': role2actor,
        'owner': True,
        'actor': actor
    })


@login_required(login_url='login')
def employer_profile_page(request):
    if not hasattr(request.user, 'employer'):
        return redirect('index')

    employer = request.user.employer

    if request.method == 'POST':
        form = None
        if request.POST.get('profile') is not None:
            form = EmployerModelForm(request.POST, instance=employer)

        elif request.POST.get('role') is not None:
            role = Role(creator=request.user.employer)
            form = RoleModelForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved")
        else:
            messages.error(request, form.errors)

    profile_form = EmployerModelForm(instance=employer)
    role_form = RoleModelForm()
    roles = Role.objects.filter(creator=request.user.employer).order_by("-id")
    return render(request, "main/employer_profile.html", context={
        'profile_form': profile_form,
        'role_form': role_form,
        'roles': roles,
    })


@login_required(login_url='login')
def actors_page(request):
    if not hasattr(request.user, 'employer'):
        return redirect('index')

    if request.method == 'POST':
        r2a = RequestRoleToActor(role_id=int(request.POST['role_id']), actor_id=int(request.POST['actor_id']))
        r2a.save()
    actors_set = Actor.objects.all()
    actor_filter = ActorFilter(request.GET, queryset=actors_set)
    actors_set = actor_filter.qs.order_by("-id")

    roles = Role.objects.filter(creator=request.user.employer)
    return render(request, "main/actors.html", context={
        'filter': actor_filter,
        'actors': actors_set,
        'roles': roles,
    })


@login_required(login_url='login')
def roles_page(request):
    if not hasattr(request.user, 'actor'):
        return redirect('index')

    if request.method == 'POST':
        a2r = RequestActorToRole(actor_id=request.POST['actor_id'], role_id=request.POST['role_id'])
        a2r.save()

    roles_set = Role.objects.all()
    roles_filter = RoleFilter(request.GET, queryset=roles_set)
    roles_set = roles_filter.qs.order_by("-id")
    return render(request, "main/roles.html", context={
        'filter': roles_filter,
        'roles': roles_set,
    })


@login_required(login_url='login')
def role_page(request, role_id):
    role = Role.objects.get(id=role_id)
    if role is None or not hasattr(request.user, 'employer') or role.creator != request.user.employer:
        return redirect('index')
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('Accept') is not None:
            a2r = RequestActorToRole.objects.get(id=request.POST['Accept'])
            a2r.accept()
            a2r.save()
        elif request.POST.get('Deny') is not None:
            a2r = RequestActorToRole.objects.get(id=request.POST['Deny'])
            a2r.deny()
            a2r.save()

    actor2role = RequestActorToRole.objects.filter(role=role, is_accepted=False, is_denied=False).order_by("-id")
    role2actor = RequestRoleToActor.objects.filter(role=role).order_by("-id")

    return render(request, "main/employer_profile.html", context={
        'role': role,
        'actor2role': actor2role,
        'role2actor': role2actor
    })
