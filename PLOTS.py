import matplotlib.pyplot as plt
from datetime import datetime
import os
from PIL import Image
import streamlit as st


def plot_1D(figure, ax, ch, entries, title, run_number,  xlabel, ylabel, chamber_number = '', xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
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
        
    xticks : list, optional
        Labels of x axis ticks. The default value is for 1 MiniDT chamber channels
    
    chamber_number : string, optional
        chamber number, to distinguish the two chambers monitors. The default is '' since only one is working at the moment

    
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


    
def plot_2D(figure, ax, entries, title, run_number, xlabel, ylabel, chamber_number):
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
    
    chamber_number : string, optional
        chamber number, to distinguish the two chambers monitors

    
    Returns
    -------
    None.  
      
    """
    run_title = "Run " + str(run_number)
    scale_max = 1.1*entries.max()
    scale_min = .9*entries.min()
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax.set_yticks([1, 2, 3, 4])
    ax.pcolormesh(entries, vmin = scale_min, vmax = scale_max) 
    ax.set_title(run_title + ' - ' + datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()


def save_1D(path, ch, entries, title, namerun, xlabel, ylabel, chamber_number, xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
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
    
    xticks : list, optional
        Labels of x axis ticks. The default value is for 1 MiniDT chamber channels
        
    chamber_number : string
        chamber number, to distinguish the two chambers monitors

    Returns
    -------
    None.
    
    """
    
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks(xticks)
    ax_s.bar(ch,entries, width =1, color = '#1f77b4', align ='center')
    ax_s.set_title(namerun + ' - ' + chamber_number + ' - '+datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(path +chamber_number+'_'+title+'.PNG') 
    plt.close()
    
def save_2D(path, entries, title, namerun , xlabel, ylabel, chamber_number):
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
    
    chamber_number : string
        chamber number, to distinguish the two chambers monitors

        
    Returns
    -------
    None.
        
    """
    
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    scale_max = 1.1*entries.max()
    scale_min = .9*entries.min()
    ax_s.cla()
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax_s.set_yticks([1, 2, 3, 4])
    m = ax_s.pcolormesh(entries, vmin = scale_min, vmax = scale_max) 
    plt.colorbar(m, ax = ax_s)
    ax_s.set_title(namerun + ' - ' + chamber_number + ' - '+ datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(path +chamber_number+'_'+title+'.PNG') 
    plt.close()

def make_monitor( path, image_names , monitor_name , chamber_number):
    """
    

    Parameters
    ----------
    path : string
        path to the directory in which the produced image will be saved
        
    image_names : list
        list of all the images to put in the monitor 
        
    monitor_name : string
        string with image name 
        
    chamber_number : string
        chamber number, to distinguish the two chambers monitors

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
     

    title = chamber_number+'_'+monitor_name+'_monitor.PNG'

    
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
            c= st.container()
            c.markdown("#### Chamber 7")
            c.image(images[0])
            c.markdown("#### Chamber 8")
            c.image(images[1])
            #print('ok', flush = True)
        if len(images) == 4:
            with fig_col2:
                st.markdown("### Timebox and Scintillator Occupancy")
                c= st.container()
                c.markdown("#### Chamber 7")
                c.image(images[2])
                c.markdown("#### Chamber 8")
                c.image(images[3])
                #print('ok', flush = True)
    os.chdir( original_path)
    


def draw_digis_onech(x0, y0, hits_channels):
    """
    

    Parameters
    ----------
    x0 : int
        x coordinate of the lower left corner of the chamber representation
        
    y0 : int
        x coordinate of the lower left corner of the chamber representation
        
    hits_channels : list
        list of channels of hits in chamber for the given event

    Returns
    -------
    None.

    """
    layer=[4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1,4,2,3,1]
    wire=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16]
    cells={}
    wires={}
    b=42
    h=13
    off=[0,-b/2,0,-b/2]
    #print([p[0] for pp in pat for p in pp])
    for ch in range(0,64):
        l=layer[ch]
        w=wire[ch]
        x=b*(w-1)+off[l-1]+x0
        y=h*(l-1)+y0

        if (ch in hits_channels): 
            mfc='aquamarine'
        else:
            mfc='w'
        cells['L'+str(l)+'W'+str(w)]=plt.Rectangle((x,y),b,h,ec='k',fc=mfc)
        wires['L'+str(l)+'W'+str(w)]=plt.Circle((x+b/2,y+h/2),radius=1,fc='k')
        plt.gca().add_patch(cells['L'+str(l)+'W'+str(w)])
        plt.gca().add_patch(wires['L'+str(l)+'W'+str(w)])
        
def event_display(displaypath, n_event, hits_ch7, hits_ch8):
    """
    

    Parameters
    ----------
    displaypath : string
        path to folder in which the event diplay will be saved
    
    n_event : int
        event number in current monitor run
        
    hits_ch7 : list
        hits in chamber 7
        
    hits_ch8 : list
        hits in chamber 8

    Returns
    -------
    None.

    """
    plt.figure(figsize=(12, 12), dpi=300)
    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    plt.tick_params(bottom = False, left=False)      
    draw_digis_onech(0, 160, hits_ch8)
    draw_digis_onech(0, 0, hits_ch7)
    plt.axis('scaled')
    title = displaypath+'Event_'+str(n_event)+'.PNG'
    plt.savefig(title)


    
    

    