from ppt.generator import PPTGenerator

def main():
    topic = input("Enter the topic for the presentation: ")

    while True:
      try:
          num_slides = int(input("Enter the number of slides :"))
          break
      except ValueError:
          print("Invalid input. Please enter a valid number.")

    output_file = input("Enter the output file name (default is 'generated_presentation.pptx'): ")

    if not output_file:
        output_file = "generated_presentation.pptx"

    generator = PPTGenerator()
    print("PPT Generator initialized successfully!")

    output_file = generator.generate_presentation(topic, num_slides, output_file)
    print(f"Presentation saved as: {output_file}")

if __name__ == "__main__":
    main()
