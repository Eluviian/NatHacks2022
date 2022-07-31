import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_byprop
import matplotlib as mp
from multiprocessing import Process, Queue,set_start_method
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, DetrendOperations, FilterTypes

# total_data = np.array()
class Data:
    def __init__(self):
        self.newData = None
        
    def sendingdata(self, data, num_channels):
        # board_id = 38
        # sampling_rate = BoardShim.get_sampling_rate(board_id)
        self.newData = data[num_channels, :].T
        

        

    def find_alpha_beta_ratio(self):
        if self.newData != None:
            array_2d = np.array(self.newData)
        # combined_array = np.concatenate(total_data, data_to_save_2d)
            array_1d = array_2d.flatten()   
            

    # for channel in enumerate(num_channels):
    # # plot timeseries
    #     if len(data_to_save) != 0:
    #         DataFilter.detrend(data_to_save[channel], DetrendOperations.CONSTANT.value)
    #         DataFilter.perform_bandpass(
    #             data_to_save[channel],
    #             sampling_rate,
    #             1.0,
    #             40.0,
    #             2,
    #             FilterTypes.BUTTERWORTH.value,
    #             0,
    #         )
    
    
    