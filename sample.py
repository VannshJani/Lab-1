import pdb
import src
import glob
import importlib.util as ut
import os
import cv2



### Change path to images here
path = '/Users/vannshjani/Desktop/CV3/ES666-Assignment3/Images/*'  # Use os.sep, Windows, linux have different path delimiters
###

all_submissions = glob.glob('./src/*')
os.makedirs('./results/', exist_ok=True)
for idx,algo in enumerate(all_submissions):
    print('****************\tRunning Awesome Stitcher developed by: {}  | {} of {}\t********************'.format(algo.split(os.sep)[-1],idx,len(all_submissions)))
    try:
        module_name = '{}_{}'.format(algo.split(os.sep)[-1],'stitcher')
        filepath = '{}{}stitcher.py'.format( algo,os.sep,'stitcher.py')
        spec = ut.spec_from_file_location(module_name, filepath)
        module = ut.module_from_spec(spec)
        spec.loader.exec_module(module)
        PanaromaStitcher = getattr(module, 'PanaromaStitcher')
        inst = PanaromaStitcher()

        ###
        scale_factors = [0.25,1,1,0.5,0.5,1]
        scale_idx = 0 
        for impaths in sorted(glob.glob(path)):
            print('\t\t Processing... {}'.format(impaths))
            stitched_image, homography_matrix_list = inst.make_panaroma_for_images_in(path=impaths,scale_factor_x=scale_factors[scale_idx],scale_factor_y=scale_factors[scale_idx])
            scale_idx+=1
            outfile =  './results/{}/{}.png'.format(impaths.split(os.sep)[-1],spec.name)
            os.makedirs(os.path.dirname(outfile),exist_ok=True)
            cv2.imwrite(outfile,stitched_image)
            print(homography_matrix_list)
            print('Panaroma saved ... @ ./results/{}.png'.format(spec.name))
            print('\n\n')

    except Exception as e:
        print('Oh No! My implementation encountered this issue\n\t{}'.format(e))
        print('\n\n')
