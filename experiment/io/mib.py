# -*- coding: utf-8 -*- 

"""
用于测试读取 MIB 文件
"""
import os 
import numpy as np

mib_path = "D:\\FourDExplorerData\\Data\\04_Combined Test_x500k_cl25cm_cl1_4_df.mib"
hdr_path = "D:\\FourDExplorerData\\Data\\04_Combined Test_x500k_cl25cm_cl1_4_df.hdr"


def parseHDR(hdr_path: str):
    pass 

def parseMIBHDR(mib_path):
    with open(mib_path, 'rb') as file:
        # head = file.read(1024).decode().split(',')
        head_str = file.read(1024).decode()
        head_test = head_str.split(',')
        # test if single
        if head_test[2] == "00384":
            head_size = 384
            assembly_size = "single"
        elif head_test[2] == "00768":
            head_size = 768
            assembly_size = "quad"
        # file.seek(0)
        # parts = [p for p in file.read(1024).decode()[:head_size].split(',') if '\x00' not in p]
        # print(file.read(1024).decode()[:head_size].split(','))
        # head = parts 

        head = [p for p in head_str[0:head_size].split(',') if '\x00' not in p]
        
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        print(f"file_size: {file_size}")
        merlin_size = (int(head[4]), int(head[5]))
        print(f"merlin_size: {merlin_size}")
        raw = (head[6] == "R64")
        print(f"raw: {raw}")
        if head[7].endswith("2x2"):
            detector_geometry = "2x2"
        elif head[7].endswith("Nx1"):
            detector_geometry = "Nx1"
        print(f"detector_geometry: {detector_geometry}")
        
        chip_num = head[3]
        print(f"chip_num: {chip_num}")
        print(f"head_size: {head_size}")
        print(f"assembly_size: {assembly_size}")
        
        # set bit-depths for processed data (binary is U08 as well)
        if not raw:
            if head[6] == "U08":
                dtype = np.dtype(">u1").name 
                dynamic_range = "1 or 6 bit"
            elif head[6] == "U16":
                dtype = np.dtype(">u2").name 
                dynamic_range = "12-bit"
            elif head[6] == "U32":
                dtype = np.dtype(">u4").name 
                dynamic_range = "24-bit"
        print(f"dtype: {dtype}")
        print(f"dynamic_range: {dynamic_range}")
        
        # print(f"exposure_in_ns: {head[-3]}")
        # exposure = float(head[-3][:-2]) / 1e6
        # print(f"exposure: {exposure} ms")

        timestamp = head[-3]
        print(f"timestamp: {timestamp}")

        print(f"head: {head}")
        
        # file.seek(0)
        # head_384 = file.read(384).decode().split(',')
        # print(f"head_384: {head_384}")
        
        # file.seek(0)
        # head_768 = file.read(768).decode().split(',')
        # print(f"head_768: {head_768}")
        

        if raw:
            bits_per_pixel_raw = int(head[-1])
            size_factors = {
                1: 1/8,
                6: 1,
                12: 2,
                24: 4,
            }
            size_factor = size_factors[bits_per_pixel_raw]
            # if bits_per_pixel_raw == 24:
            #     image_size = (image_size[0], image_size[1] // 2)
            # image_size_bytes = int(image_size[0] * image_size[1] * size_factor)
            # num_images = file_size // (image_size_bytes + head_size)
        else:
            bytes_per_pixel = np.dtype(dtype).itemsize
            image_size_bytes = merlin_size[0] * merlin_size[1] * bytes_per_pixel
            num_images = file_size // (image_size_bytes + head_size)
        print(f"num_images: {num_images}")

            


def loadMIBDataset(mib_path):
    pass 

if __name__ == "__main__":
    parseMIBHDR(mib_path)   