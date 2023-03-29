from django.shortcuts import render
from transformers import pipeline, set_seed

set_seed(42)

generator = pipeline('text-generation', model='gpt2')

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        chatbot_response = generate_response(user_input)
        context = {'user_input': user_input, 'chatbot_response': chatbot_response}
        return render(request, 'chat/home.html', context)
    else:
        return render(request, 'chat/home.html')

def generate_response(prompt, max_length=100):
    response = generator(prompt, max_length=max_length, do_sample=True, temperature=0.7)[0]['generated_text']
    return response.strip()
