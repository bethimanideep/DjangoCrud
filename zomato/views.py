from django.shortcuts import render, redirect
from django.http import JsonResponse

users = [
    {"id": 1, "name": "Mani", "age": 23, "city": "Warangal", "editing": False},
    {"id": 2, "name": "Alice", "age": 28, "city": "New York", "editing": False},
    {"id": 3, "name": "Mani", "age": 23, "city": "Warangal", "editing": False},
    {"id": 4, "name": "Alice", "age": 28, "city": "New York", "editing": False}
    # ... other users ...
]


def user_list(request):
    return render(request, 'zomato/listuser.html', {'users': users})


def set_editing(request):
    user_id = int(request.GET.get('id', -1))
    success = False
    for user in users:
        if user['id'] == user_id:
            user['editing'] = True
            success = True
        else:
            user['editing'] = False
    return JsonResponse({'success': success})


def confirm_edit(request, user_id):
    if request.method == 'POST':
        for user in users:
            if user['id'] == int(user_id):
                user['name'] = request.POST.get('name')
                user['age'] = int(request.POST.get('age'))
                user['city'] = request.POST.get('city')
                user['editing'] = False
                break
    return redirect('zomato:user-list')

# ... other views ...


def add(request):
    return render(request, "zomato/adduser.html")


def homepage(request):
    return render(request, "zomato/homepage.html")
    # ... (existing code)


def delete_user(request, user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            break
    return redirect('zomato:user-list')


def edit_user(request, user_id):
    for user in users:
        if user['id'] == user_id:
            return render(request, 'zomato/edituser.html', {'user': user})
    return redirect('zomato:user-list')


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        city = request.POST.get('city')
        new_user = {"id": len(users) + 1, "name": name,
                    "age": age, "city": city, "editing": False}
        users.append(new_user)
        return redirect('zomato:user-list')  # Redirect to the user list page
    return render(request, "zomato/adduser.html")
