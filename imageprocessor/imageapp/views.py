from django.shortcuts import render

# Create your views here.

import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        # Get the image from the request
        image_file = request.FILES.get('image')
        if image_file:
            # Simulate heavy computation by sleeping
            time.sleep(5)

            # Process the image (replace this with your actual image processing code)
            img = Image.open(image_file)
            width, height = img.size
            result = {'width': width, 'height': height}

            # Return the results as JSON response
            return JsonResponse(result)
        else:
            return JsonResponse({'error': 'No image provided'}, status=400)
    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)

