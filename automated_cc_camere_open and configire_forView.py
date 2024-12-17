import pyautogui
import time

# Give some time to switch to the screen where the image is located
time.sleep(3)

# Specify the paths to your images
image_path = r"S1.png"
hfl_path = r"hfl.png"
view_set = r"asn_move.png"
chanel_set = r"sixtyfour.png"  # New image location
screen_set = r"screen.png"  # Fullscreen image location

# Define the coordinates for the view_set_image location
view_set_image_x = 100  # Example X coordinate
view_set_image_y = 200  # Example Y coordinate



# Locate all occurrences of the first image on the screen
locations = list(pyautogui.locateAllOnScreen(image_path))

# Check if any locations were found
if locations:
    for location in locations:
        # Get the center of each found location
        center = pyautogui.center(location)
        print(f"Found {image_path} at: {center}")
        
        # Move to the center and click
        pyautogui.moveTo(center, duration=0.5)  # Smooth mouse movement
        time.sleep(0.5)  # Wait before clicking
        pyautogui.click()
        time.sleep(1)  # Wait for a second after the click to allow the UI to respond
        
        # Move to the view_set_image location and click
        pyautogui.moveTo(view_set_image_x, view_set_image_y, duration=0.5)
        time.sleep(0.5)  # Wait before clicking
        pyautogui.click()  # Click at the view_set_image location
        time.sleep(1)  # Wait for a second to allow the UI to respond
        
        # Now locate the second image (hfl)
        hfl_location = pyautogui.locateOnScreen(hfl_path)
        
        if hfl_location:
            hfl_center = pyautogui.center(hfl_location)
            print(f"Found {hfl_path} at: {hfl_center}")
            pyautogui.moveTo(hfl_center, duration=0.5)  # Smooth mouse movement
            time.sleep(0.5)  # Wait before clicking
            pyautogui.doubleClick()
            time.sleep(1)  # Wait for a second to allow the UI to respond
            
            # Now locate the view_set image
            view_location = pyautogui.locateOnScreen(view_set)
            if view_location:
                view_center = pyautogui.center(view_location)
                print(f"Found {view_set} at: {view_center}")
                pyautogui.moveTo(view_center, duration=0.5)  # Smooth mouse movement
                time.sleep(0.5)  # Wait before clicking
                pyautogui.click()  # Click on the view_set image
            else:
                print(f"{view_set} not found on the screen.")    
        else:
            print(f"{hfl_path} not found on the screen.")
else:
    print(f"{image_path} not found on the screen.")

# Wait for the user to select another image
print("Please move the cursor to the new image you want to select.")
time.sleep(5)  # Wait for 5 seconds to allow the user to position the cursor

# Locate the new image (chanel_set) on the screen
chanel_location = pyautogui.locateOnScreen(chanel_set)

if chanel_location:
    chanel_center = pyautogui.center(chanel_location)
    print(f"Found {chanel_set} at: {chanel_center}")
    pyautogui.moveTo(chanel_center, duration=0.5)  # Smooth mouse movement
    time.sleep(0.5)  # Wait before clicking
    pyautogui.click()  # Click on the chanel_set image
    print(f"Clicked at the new image location: {chanel_center}")

    # Locate the fullscreen image (screen_set)
    screen_location = pyautogui.locateOnScreen(screen_set)

    if screen_location:
        screen_center = pyautogui.center(screen_location)
        print(f"Found {screen_set} at: {screen_center}")
        pyautogui.moveTo(screen_center, duration=0.5)  # Smooth mouse movement
        time.sleep(0.3)  # Wait before clicking
        pyautogui.doubleClick()  # Click on the screen_set image