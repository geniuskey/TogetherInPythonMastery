import  os
import exapp


def main():
    examples_path = os.path.join(os.path.dirname(__file__), "examples")
    exapp.main_gui(examples_path, "함께해요 파이썬 전문가")


if __name__ == '__main__':
    main()