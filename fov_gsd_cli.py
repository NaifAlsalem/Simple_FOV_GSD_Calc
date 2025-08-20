import argparse
import math

def calculate_fov(sensor_width, focal_length):
    """Calculate field of view in degrees."""
    fov_rad = 2 * math.atan(sensor_width / (2 * focal_length))
    return math.degrees(fov_rad)

def calculate_gsd(fov_deg, altitude):
    """Calculate ground sampling distance in meters."""
    fov_rad = math.radians(fov_deg)
    return altitude * math.tan(fov_rad / 2)

def main():
    parser = argparse.ArgumentParser(description="Compute FOV and GSD for a sensor.")
    parser.add_argument("sensor_width", type=float, help="Sensor width (mm)")
    parser.add_argument("focal_length", type=float, help="Focal length (mm)")
    parser.add_argument("altitude", type=float, help="Altitude above ground (m)")
    args = parser.parse_args()

    fov_deg = calculate_fov(args.sensor_width, args.focal_length)
    gsd = calculate_gsd(fov_deg, args.altitude)

    print(f"FOV: {fov_deg:.2f} degrees")
    print(f"GSD: {gsd:.2f} m")

if __name__ == "__main__":
    main()
