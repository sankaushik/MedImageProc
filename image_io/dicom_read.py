#-----------------------------------------------------------------------------
# dicom_read.py
#-----------------------------------------------------------------------------
# Read a single DICOM series and create an ITK image object
#
#
# Sandeep Kaushik; SanKaushik.S@gmail.com
#-----------------------------------------------------------------------------


import SimpleITK as sitk


def dicom_series_read(in_dir):
    