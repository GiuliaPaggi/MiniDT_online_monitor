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
    
    fig, ax = plt.subplots(1, 1, figsize = (15, 10))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(xticks)
    ax.bar(ch,entries, width =1, color = '#1f77b4', align ='center')
    ax.set_title(namerun + ' - ' + chamber_number + ' - '+datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig.savefig(path +chamber_number+'_'+title+'.PNG') 
    plt.close()
    
def save_2D(path, entries, title, namerun , xlabel, ylabel, chamber_number):
    """    
    The function plots and saves as .PNG the a 2D histogram given the entries of each bin. 
    
    ----------          
    Parameters
    ----------
    path : string
        path to the directory in which the plot will be saved 
    
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
    
    fig, ax= plt.subplots(1, 1, figsize = (15, 10))
    scale_max = 1.1*entries.max()
    scale_min = .9*entries.min()
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax.set_yticks([1, 2, 3, 4])
    m = ax.pcolormesh(entries, vmin = scale_min, vmax = scale_max) 
    plt.colorbar(m, ax = ax)
    ax.set_title(namerun + ' - ' + chamber_number + ' - '+ datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig.savefig(path +chamber_number+'_'+title+'.PNG') 
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
    
    
def update_monitor(path, placeholder, image_names, rate_, rate_scint):
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
    
    rate_scint : string
        rate of scintillator in the last 30s of data taking
        
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
        st.markdown("#### Rate: "+rate_+" Hz  &emsp;&emsp; Scintillator Rate: "+rate_scint+" Hz")
        #st.markdown("### Scintillator Rate: "+rate_scint+" Hz")
        fig_col1, fig_col2 = st.columns([2, 3])
        with fig_col1:
            st.markdown("#### Occupancy Monitor")
            c= st.container()
            c.markdown("#### Chamber 7")
            c.image(images[0])
            c.markdown("#### Chamber 8")
            c.image(images[1])
            #print('ok', flush = True)
        if len(images) == 4:
            with fig_col2:
                st.markdown("#### Timebox and Scintillator Occupancy")
                c= st.container()
                c.markdown("#### Chamber 7")
                c.image(images[2])
                c.markdown("#### Chamber 8")
                c.image(images[3])
                #print('ok', flush = True)
    os.chdir( original_path)
    


def draw_digis_onech(figure, ax, x0, y0, hits_channels):
    """
    
    Parameters
    ----------
    figure: Figure
        Figure in which the event display is drawn
        
    ax : AxesSubplot
        Axes of the figure in which the function draws
        
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
        ax.add_patch(cells['L'+str(l)+'W'+str(w)])
        ax.add_patch(wires['L'+str(l)+'W'+str(w)])
        
def event_display(displaypath, n_file,  hits_ch7, info_ch7, hits_ch8, info_ch8, namerun, n_event ):
    """
    
    Parameters
    ----------
    displaypath : string
        path to folder in which the event display plots will be saved
        
    n_file : int
        int to numerate file in the folder
        
    hits_ch7 : list
        list of hits in chamber 7
        
    hits_ch8 : list
        list of hits in chamber 8
        
    namerun : string
        run name to set the event display title
        
    n_event : int
        number of 4 hits in 2 chamber events since the beginning of the monitor program 
    Returns
    -------
    None.
    """
    fig, ax = plt.subplots(1, 1, figsize = (15, 10))
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.tick_params(bottom = False, left=False)      
    draw_digis_onech(fig, ax, 0, 365, hits_ch8)
    draw_digis_onech(fig, ax, 0, 0, hits_ch7)
    ax.set_title(namerun +' - Event n.'+ str(n_event))
    ax.text(0.1, -0.2,  info_ch7,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
    ax.text(0.6, -0.2,info_ch8,
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
    ax.axis('scaled')
    title = displaypath+'Event_Display_'+str(n_file)+'.PNG'
    fig.savefig(title)
    plt.close()