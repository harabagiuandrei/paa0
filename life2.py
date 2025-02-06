import concurrent.futures
import cv2
import time
import see from see

class Life:
    def __init__(self, f, s):
        self.first = f
        self.second = s
        self.alive = True

    def self_action(self):
        # Perform actions based on sensory inputs in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(self.see),
                executor.submit(self.smell),
                executor.submit(self.feel)
            ]
            for future in concurrent.futures.as_completed(futures):
                print(future.result())
    

    def see(self):
        print("Seeing...")
        # Simulate vision processing (e.g., OpenCV operations)
        time.sleep(1)
        # frame = "frame_data"  # Placeholder for actual frame data
        frame = self.see.whatDoYouSee()

        self.what_do_you_see(frame)
        return "Vision processed"

    def smell(self):
        print("Smelling...")
        # Simulate smell processing
        time.sleep(1)
        smell_data = "floral scent"
        self.what_do_you_smell(smell_data)
        return "Smell processed"

    def feel(self):
        print("Feeling...")
        # Simulate tactile processing
        time.sleep(1)
        tactile_data = "smooth surface"
        self.what_do_you_feel(tactile_data)
        return "Tactile processed"

    def what_do_you_see(self, frame):
        print("Processing vision input...")

    def what_do_you_smell(self, smell_data):
        print(f"Processing smell input: {smell_data}")

    def what_do_you_feel(self, tactile_data):
        print(f"Processing tactile input: {tactile_data}")

def live(life_instance):
    while life_instance.alive:
        life_instance.self_action()

# Instantiate the Life class and run the lifecycle
life_instance = Life("example_first", "example_second")
live(life_instance)