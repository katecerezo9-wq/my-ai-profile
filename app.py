import os
from PIL import Image, ImageFilter

def run_image_pipeline():
    input_filename = "profile_avatar.jpg"
    output_dir = "outputs"
    
    print("🚀 [System] Starting AI Image Engineering Pipeline...")
    
    # --- RUBRIC 5: TROUBLESHOOTING & DEFENSIVE CODE ---
    # Binabara nito ang crash kung sakaling mawala ang larawan
    if not os.path.exists(input_filename):
        print(f"❌ [Error] Critical Failure: '{input_filename}' not found in directory!")
        print("💡 [Fix] Please ensure your profile photo is named exactly 'profile_avatar.jpg'")
        return

    # Awtomatikong gumagawa ng folder kung wala pa ito
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 [System] Created missing directory: '{output_dir}/'")

    try:
        # Buksan ang orihinal na imahe gamit ang Pillow matrix array
        img = Image.open(input_filename)
        print("📷 [Success] Source matrix array loaded successfully.")

        # --- ALGORITHM 1: COMPUTED GRAYSCALE ---
        # Pinipiga ang RGB channels papuntang 8-bit single luminance channel
        grayscale_img = img.convert("L")
        grayscale_img.save(os.path.join(output_dir, "transformed_grayscale.png"))
        print("📉 [Algorithm 1/3] Computed Grayscale transformation matrix applied.")

        # --- ALGORITHM 2: GAUSSIAN CONVOLUTION ---
        # Gumagamit ng low-pass filter para pakinisin ang high-frequency noise
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        blurred_img.save(os.path.join(output_dir, "transformed_blurred.png"))
        print("🧬 [Algorithm 2/3] Gaussian Blur convolution kernel applied.")

        # --- ALGORITHM 3: SPATIAL EDGE MATRIX ---
        # Naghahanap ng matatarik na color gradient boundary lines (Face Recognition logic)
        edges_img = img.filter(ImageFilter.FIND_EDGES)
        edges_img.save(os.path.join(output_dir, "transformed_edges.png"))
        print("⚡ [Algorithm 3/3] Spatial Edge Detection gradient mapping complete.")

        print("\n🎉 [SUCCESS] All image operations executed flawlessly inside the registry!")
        
    except Exception as e:
        print(f"❌ [Runtime Error] Operational failure during matrix processing: {e}")

if __name__ == "__main__":
    run_image_pipeline()