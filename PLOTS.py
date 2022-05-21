import matplotlib.pyplot as plt
from datetime import datetime

def occupancy_1D(figure, ax, ch, entries, title):
    """    
    The function plots the histogram of the occupancy of 64 channels (1 MiniDT chamber) 
    
    ----------          
    Parameters
    ----------
    figure: Figure
        Figure in which the subplots are drawn
        
    ax : AxesSubplot
        Axes of the subplot in which the function draws
          
    ch : array-like
         X bins of the bar plot
    
    entr : array-like
        Height of the bars
    
    title : string
        Title of the plot
        
    """
       
    ax.cla()
    ax.bar(ch,entries, width =1, color = '#1f77b4')
    ax.set_title(datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()
    extent = ax.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    figure.savefig(title+'.PNG', bbox_inches=extent.expanded(1.1, 1.2))

    
def occupancy_2D(figure, ax, entries, title):
    """    
    The function plots the 2D occupancy of 64 channels (1 MiniDT chamber) 
    
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
        
    """

    ax.cla()
    ax.pcolormesh(entries)       
    ax.set_title(datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()
    extent = ax.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    figure.savefig(title+'.PNG', bbox_inches=extent.expanded(1.1, 1.2))