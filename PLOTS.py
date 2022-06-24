import matplotlib.pyplot as plt
from datetime import datetime
import os
from PIL import Image
import streamlit as st


def plot_1D(figure, ax, ch, entries, title, run_number,  xlabel, ylabel, xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
    """    
    The function plots and shows 1D histograms given the x axis and the entries of each bin.
    
    ----------          
    Parameters
    ----------
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
          
    ch : list
         X bins of the bar plot
    
    entries : list
        Height of the bars
    
    title : string
        Title of the plot
        
    run_number : string
        Run number to complete the title of the plot 
       
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
        
    xticks : list
        Labels of x axis ticks. The default value is for 1 MiniDT chamber channels.
    
    Returns
    -------
    None.
    
    """
    run_title = "Run " + str(run_number) 
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(xticks)
    ax.bar(ch,entries, width =1, color = '#1f77b4', align ='center')
    ax.set_title(run_title + ' - ' +datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()


    
def plot_2D(figure, ax, entries, title, run_number, xlabel, ylabel):
    """    
    The function plots and shows the a 2D histogram given the entries of each bin. 
    
    ----------          
    Parameters
    ----------
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
    
    entries : array-like
        Height of the bars
    
    title : string
        Title of the plot
        
    run_number : string
        Run number to complete the title of the plot 
   
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
    
    Returns
    -------
    None.  
      
    """
    run_title = "Run " + str(run_number) 
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax.set_yticks([1, 2, 3, 4])
    ax.pcolormesh(entries) 
    ax.set_title(run_title + ' - ' + datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()


def save_1D(path, ch, entries, title, namerun, xlabel, ylabel, xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
    """    
    The function plots and saves as .PNG the a 1D histogram given the entries of each bin.  
    
    ----------          
    Parameters
    ----------
    path : string
        path to the directory in which the plot will be saved
        
    ch : list
         X bins of the bar plot
    
    entries : list
        Height of the bars
    
    title : string
        Title of the plot
        
    namerun : string
        Name of the run to complete the title of the plot 
    
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
    
    xticks : list
        Labels of x axis ticks. The default value is for 1 MiniDT chamber channels.
        
    Returns
    -------
    None.
    
    """
    
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks(xticks)
    ax_s.bar(ch,entries, width =1, color = '#1f77b4', align ='center')
    ax_s.set_title(namerun + ' - ' +datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(path +title+'.PNG') 
    plt.close()
    
def save_2D(path, entries, title, namerun , xlabel, ylabel):
    """    
    The function plots and saves as .PNG the a 2D histogram given the entries of each bin. 
    
    ----------          
    Parameters
    ----------
    path : string
        path to the directory in which the plot will be saved
    
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
    
    entries : array-like
        Height of the bars
    
    title : string
        Title of the plot
    
    namerun : string
        Name of the run to complete the title of the plot 
    
    xlabel : string
        Label of x axis
    
    ylabel : string
        Label of y axis
        
    Returns
    -------
    None.
        
    """
    
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    ax_s.cla()
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax_s.set_yticks([1, 2, 3, 4])
    m = ax_s.pcolormesh(entries) 
    plt.colorbar(m, ax = ax_s)
    ax_s.set_title(namerun + ' - '+ datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(path+title+'.PNG')
    plt.close()

def make_monitor( path, image_names , monitor_name , chamber_number = ''):
    """
    

    Parameters
    ----------
    path : string
        path to the directory in which the produced image will be saved
        
    image_names : list
        list of all the images to put in the monitor 
        
    title : string
        string with image name 
        
    chamber_number : strng, optional
        chamber number, to distinguish the two chambers monitors. The default is '' since only one is working at the moment.

    Returns
    -------
    None.

    """
    original_path = os.getcwd()
    os.chdir(path)
    images = [Image.open(x) for x in image_names]
    widths, heights = zip(*(i.size for i in images))

    total_width = int(sum(widths)*.5)
    max_height = max(heights)*2

    new_im = Image.new('RGB', (total_width, max_height))

    cut = int(len(images)*.5)
    first_row = images[:cut]
    second_row = images[cut:]

    x_offset = 0
    for i in range(cut):
      new_im.paste(first_row[i], (x_offset,0))
      new_im.paste(second_row[i], (x_offset,heights[0]))
      x_offset += widths[0]
     
    if not chamber_number == '' :
        title = 'Chamber_'+chamber_number++'_'+monitor_name+'_monitor.PNG'
    else:
        title = monitor_name+'_monitor.PNG'
    
    new_im.save(title)
    os.chdir(original_path)
    
    
def update_monitor(path, placeholder, image_names, rate_):
    """
    

    Parameters
    ----------
    path : string
        path to the directory in which the images to be shown are
        
    placeholder : streamlit container
        a container that holds a single element, used to replace same element
        
    image_names : list
        list of images to be shown in the monitor window.
    
    rate_ : string
        rate in the last 30s of data taking


    Returns
    -------
    None.

    """
    #reads images
    original_path = os.getcwd()
    os.chdir(path)

    images = [Image.open(x) for x in image_names]
    #updates monitor web page
    with placeholder.container():
        st.markdown("### Rate: "+rate_+" Hz")
        fig_col1, fig_col2 = st.columns([2, 3])
        with fig_col1:
            st.markdown("### Occupancy Monitor")
            st.image(images[0])
            
        with fig_col2:
            st.markdown("### Timebox and Scintillator Occupancy")
            st.image(images[1])
    os.chdir( original_path)


    