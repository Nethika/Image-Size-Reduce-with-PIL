 # Reduce Image Size with PIL

 ## To Run:

```python size_reducer.py [input_folder_path] --out_path [output_folder_path] --width [pixel width an integer]``` 

 Examples:

 ```python size_reducer.py large_images --out_path small_images --width 200```

 ```python size_reducer.py C:\Users\NethikaSuraweera\Pictures\EOS\rue4 --width 150```
 
 ```python size_reducer.py C:\Users\NethikaSuraweera\Pictures\EOS\rue4```
  
  
If ```--output_folder_path``` is not given, the script will create a folder name formatted: ```small_images_YYYY_MM_DD-HH_MM_SS``` in the working directory.

If --width is not given, the default output image with will be 200 pixels.


Script looks for the file formats listed in line 31:

```ext = (".jpg", ".png", ".jpeg", ".gif", ".bmp")```

You can add other extensions to the above line. 

All supported image formats are listed [here](http://pillow.readthedocs.io/en/4.1.x/handbook/image-file-formats.html).

## Requirements:

```
Pillow==5.1.0

```



 
