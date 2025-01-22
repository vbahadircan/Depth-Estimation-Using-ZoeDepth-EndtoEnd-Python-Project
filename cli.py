import argparse

from predictor import DepthEstimationModel


def main():
    parser = argparse.ArgumentParser(description="Depth Estimation using ZoeDepth")
    parser.add_argument("input_image", help="Path to input image file")
    parser.add_argument("output_image", help="Path to output image file")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depth_mapargs(args.input_image, args.output_image)
    print(result)


if __name__ == "__main__":
    main()
