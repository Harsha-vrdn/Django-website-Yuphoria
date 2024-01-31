# morsecode/views.py
from django.shortcuts import render
from .forms import MorseCodeForm
from cart.models import CartItem
from django.contrib import messages

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append(' ')
        else:
            morse_code.append(MORSE_CODE_DICT.get(char, char))
    return '\n'.join(morse_code)

def morsecode_converter(request):
    input_text = ''
    morse_code = ''
    form = MorseCodeForm()

    if request.method == 'POST':
        form = MorseCodeForm(request.POST)
        name = ""

        if form.is_valid():
            input_text = form.cleaned_data['text_input']
            morse_code = text_to_morse(input_text)
            name = input_text
            price = 10

            if request.POST.get('action') == 'AddToCart':
                CartItem.objects.create(
                    user=request.user, product_name=f"{name} Morse Code", price=price
                )
                messages.success(request, 'Item added to cart successfully!')
                return render(request, 'main.html', {'form': form, 'input_text': input_text, 'morse_code': morse_code})

    return render(request, 'main.html', {'form': form, 'input_text': input_text, 'morse_code': morse_code})




