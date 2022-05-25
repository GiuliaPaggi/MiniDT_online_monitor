import matplotlib.pyplot as plt
from datetime import datetime


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
        
    """
    run_title = "Run " + str(run_number) 
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(xticks)
    ax.bar(ch,entries, width =1, color = '#1f77b4')
    ax.set_title(run_title + ' - ' +datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()
    #extent = ax.get_window_extent().transformed(figure.dpi_scale_trans.inverted())
    #figure.savefig(title+'.PNG', bbox_inches=extent.expanded(1.3, 1.25))      #extent.expanded(1.3, 1.25)

    
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
        
    """
    run_title = "Run " + str(run_number) 
    ax.cla()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax.set_yticks([1, 2, 3, 4])
    ax.pcolormesh(entries) 
    #plt.colorbar(m, ax = ax)
    ax.set_title(run_title + ' - ' + datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    plt.pause(.0001)
    plt.show()

def save_1D(ch, entries, title, run_number, xlabel, ylabel, xticks=[0, 8, 16, 24, 32, 40, 48, 56, 63]):
    """    
    The function plots and saves as .PNG the a 1D histogram given the entries of each bin.  
    
    ----------          
    Parameters
    ----------
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
        
    """
    
    run_title = "Run " + str(run_number) 
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks(xticks)
    ax_s.bar(ch,entries, width =1, color = '#1f77b4')
    ax_s.set_title(run_title + ' - ' +datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(title+'.PNG') 
    plt.close()
    
def save_2D(entries, title, run_number , xlabel, ylabel):
    """    
    The function plots and saves as .PNG the a 2D histogram given the entries of each bin. 
    
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
        
    """
    
    run_title = "Run " + str(run_number)
    fig_s, ax_s = plt.subplots(1, 1, figsize = (15, 10))
    ax_s.cla()
    ax_s.set_xlabel(xlabel)
    ax_s.set_ylabel(ylabel)
    ax_s.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) 
    ax_s.set_yticks([1, 2, 3, 4])
    m = ax_s.pcolormesh(entries) 
    plt.colorbar(m, ax = ax_s)
    ax_s.set_title(run_title + ' - '+ datetime.now().strftime("%Y/%m/%d - %H:%M:%S")+' ' +title)
    fig_s.savefig(title+'.PNG')
    plt.close()
    