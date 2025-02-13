from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  # Import messages
from app1.models import Anime


from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from app1.models import Anime

# Existing views
from django.core.paginator import Paginator
from django.shortcuts import render
from app1.models import Anime  # Ensure you have Anime model imported

def website(request):
    query = request.GET.get('query', '')  # Get the search query from the GET parameters

    if query:
        # Filter the anime list based on the search query (case-insensitive search in title)
        animes = Anime.objects.filter(title__icontains=query)
    else:
        # If no query, show all animes
        animes = Anime.objects.all()

    # Pagination: show 6 animes per page
    paginator = Paginator(animes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'web.html', {'page_obj': page_obj, 'query': query})


def anime_list(request):
    return render(request, 'animes_list.html')

def anime_list_2(request):
    return render(request, 'animes_list2.html')

def anime_list_3(request):
    return render(request, 'animes_list3.html')

def ongoing(request):
    return render(request, 'ongoing_list.html')

def ongoing_2(request):
    return render(request, 'ongoing_list2.html')

def upcoming(request):
    return render(request, 'upcoming_list.html')

def upcoming_2(request):
    return render(request, 'upcoming_list2.html')

def completed(request):
    return render(request, 'completed_list.html')

def web_2(request):
    return render(request, 'web2.html')

def web_3(request):
    return render(request, 'web_3.html')

# User authentication views
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'register.html', {'error_message': error_message})

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Authenticate and log the user in
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)  # Correct usage of login()
            return redirect('login')  # Redirect to login page or homepage after successful registration

    # If GET request, show registration form
    return render(request, 'register.html')

from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('website')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login_list.html')


def submit_login(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Example logic to check credentials (hardcoded check)
        if username == "admin" and password == "password":
            return HttpResponse("Login successful!")
        else:
            # If credentials are incorrect, return the same login page with an error message
            error_message = "Invalid username or password, please try again."
            return render(request, 'login_list.html', {'error_message': error_message, 'username': username})
    else:
        # If GET request, show login form
        return render(request, 'login_list.html')


def password(request):
    return render(request, 'pwd.html')


# New function to fetch anime data from Jikan API v4
def fetch_anime_data(request):
    # Sample anime ID to fetch data, you can make this dynamic if needed
    anime_id = 155  # Change this to fetch a specific anime

    # Make a request to the Jikan API
    url = f'https://api.jikan.moe/v4/anime/{anime_id}'
    response = requests.get(url)

    # If the response is successful
    if response.status_code == 200:
        anime_data = response.json()
        anime = anime_data['data']

        # Save the anime data to the database
        anime_instance = Anime(
            title=anime['title'],
            description=anime['synopsis'],
            image_url=anime['images']['jpg']['image_url'],
            link=anime['url']
        )
        anime_instance.save()

        # Return the data to the template
        return render(request, 'anime_detail.html', {'anime': anime_instance})
    else:
        # Handle errors or if the API request fails
        return render(request, 'error.html', {'message': 'Failed to fetch data from Jikan API'})

# You can add other views like anime_list, homepage, etc., based on your needs

def anime_search(request):
    query = request.GET.get('query')  # Get the search query from the URL
    
    if query:
        # Fetch anime data from Jikan API based on search query
        url = f'https://api.jikan.moe/v4/anime?q={query}'
        response = requests.get(url)

        if response.status_code == 200:
            anime_data = response.json()
            anime_results = anime_data['data']  # List of matching anime

            # Render the results in a template
            return render(request, 'anime_search_results.html', {'anime_results': anime_results, 'query': query})
        else:
            return render(request, 'error.html', {'message': 'Failed to fetch data from Jikan API'})
    else:
        return render(request, 'anime_search_results.html', {'anime_results': [], 'query': query})


def anime_detail(request, anime_id):
    # Make a request to the Jikan API to get the detailed info about the anime
    url = f'https://api.jikan.moe/v4/anime/{anime_id}'
    response = requests.get(url)

    if response.status_code == 200:
        anime_data = response.json()
        anime = anime_data['data']  # Detailed information about the anime
        return render(request, 'anime_detail.html', {'anime': anime})
    else:
        return render(request, 'error.html', {'message': 'Failed to fetch data from Jikan API'})