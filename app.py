import os
from PIL import Image, ImageFilter

def transform_image(image_path, output_dir="outputs"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"[System] Created directory: {output_dir}")

    try:
        print(f"[Processing] Loading image from {image_path}...")
        original_img = Image.open(image_path)
        
        print("[Algorithm] Applying Grayscale transformation...")
        grayscale_img = original_img.convert("L")
        grayscale_img.save(f"{output_dir}/transformed_grayscale.png")
        
        print("[Algorithm] Applying Gaussian Blur matrix...")
        blurred_img = original_img.filter(ImageFilter.GaussianBlur(radius=4))
        blurred_img.save(f"{output_dir}/transformed_blurred.png")
        
        print("[Algorithm] Extracting image edges...")
        edges_img = grayscale_img.filter(ImageFilter.FIND_EDGES)
        edges_img.save(f"{output_dir}/transformed_edges.png")
        
        print("\n🎉 [Success] All image operations executed flawlessly!")

    except FileNotFoundError:
        print(f"❌ [Error] Could not find the image '{image_path}'.")
    except Exception as e:
        print(f"❌ [Unexpected Error] {e}")

if __name__ == "__main__":
    sample_image = "profile_avatar.jpg" 
    if not os.path.exists(sample_image):
        print(f"⚠️ Notice: Please place a '{sample_image}' in this folder to run the algorithm.")
    else:
        transform_image(sample_image)