#-*- coding: utf-8 -*- 
import sys 
import os 
import unittest


ROOTPATH = os.path.split(os.path.dirname(__file__))[0]
if not ROOTPATH in sys.path:
    sys.path.append(ROOTPATH)
    
from lib.Probe import OpticalSTEM

class TestProbe(unittest.TestCase):

    def test_camera_length_calculation(self):
        # Given parameters
        U = 60e3  # 60kV in V
        alpha = 22.5e-3  # 22.5 mrad in rad
        N = 128
        bright_field_disk_radius = 39
        detector_pixel_size = 150e-6  # 150 um in m

        # Create a Probe instance
        optics = OpticalSTEM(
            accelerate_voltage=U,
            detector_shape=[N, N],
            scan_shape=[N, N],
            alpha=22.5e-3,
            scan_step_size=1.0,
            bright_field_disk_radius=bright_field_disk_radius,
            detector_pixel_size=detector_pixel_size
        )
        # optics.setAccelerateVoltage(U)
        # optics.setConvergentAngle(alpha)
        # optics.setDetectorN(N)
        # optics.setDetectorPixelSize(detector_pixel_size, update_cache=True)
        

        # Calculate the expected camera length
        expected_camera_length = (bright_field_disk_radius * detector_pixel_size) / alpha

        # Get the actual camera length from the Probe instance
        actual_camera_length = optics.camera_length
        
        print(optics.camera_length)
        print(bright_field_disk_radius * detector_pixel_size / alpha )

        # Assert that the calculated camera length matches the expected value
        self.assertAlmostEqual(actual_camera_length, expected_camera_length, places=2)
        
    def test_bright_field_disk_radius_calculation(self):
        # Given parameters
        U = 60e3  # 60kV in V
        alpha = 22.5e-3  # 22.5 mrad in rad
        camera_length = 576e-3  # 576 mm in m
        detector_pixel_size = 150e-6  # 150 um in m
        N = 128

        # Create a Probe instance
        optics = OpticalSTEM(
            accelerate_voltage=U,
            detector_shape=[N, N],
            scan_shape=[N, N],
            alpha=alpha,
            camera_length=camera_length,
            detector_pixel_size=detector_pixel_size
        )

        # Calculate the expected bright_field_disk_radius
        expected_bright_field_disk_radius = (alpha * camera_length) / detector_pixel_size

        # Get the actual bright_field_disk_radius from the Probe instance
        actual_bright_field_disk_radius = optics.bright_field_disk_radius

        # Assert that the calculated bright_field_disk_radius matches the expected value
        self.assertAlmostEqual(actual_bright_field_disk_radius, expected_bright_field_disk_radius, places=2)
        
    def test_alpha_calculation(self):
        # Given parameters
        U = 60e3  # 60kV in V
        camera_length = 576e-3  # 576 mm in m
        bright_field_disk_radius = 1.5e-3  # 1.5 mm in m
        detector_pixel_size = 150e-6  # 150 um in m
        N = 128

        # Create a Probe instance without specifying alpha
        optics = OpticalSTEM(
            accelerate_voltage=U,
            detector_shape=[N, N],
            scan_shape=[N, N],
            camera_length=camera_length,
            bright_field_disk_radius=bright_field_disk_radius,
            detector_pixel_size=detector_pixel_size
        )

        # Calculate the expected alpha
        expected_alpha = (bright_field_disk_radius * detector_pixel_size) / camera_length

        # Get the actual alpha from the Probe instance
        actual_alpha = optics.alpha

        # Assert that the calculated alpha matches the expected value
        self.assertAlmostEqual(actual_alpha, expected_alpha, places=2)

    def test_detector_pixel_size_calculation(self):
        # Given parameters
        U = 60e3  # 60kV in V
        alpha = 22.5e-3  # 22.5 mrad in rad
        camera_length = 576e-3  # 576 mm in m
        bright_field_disk_radius = 1.5e-3  # 1.5 mm in m
        N = 128

        # Create a Probe instance without specifying detector_pixel_size
        optics = OpticalSTEM(
            accelerate_voltage=U,
            detector_shape=[N, N],
            scan_shape=[N, N],
            alpha=alpha,
            camera_length=camera_length,
            bright_field_disk_radius=bright_field_disk_radius
        )

        # Calculate the expected detector_pixel_size
        expected_detector_pixel_size = (alpha * camera_length) / bright_field_disk_radius

        # Get the actual detector_pixel_size from the Probe instance
        actual_detector_pixel_size = optics.detector_pixel_size

        # Assert that the calculated detector_pixel_size matches the expected value
        self.assertAlmostEqual(actual_detector_pixel_size, expected_detector_pixel_size, places=2)

if __name__ == '__main__':
    unittest.main()
