import SORT   
from hypothesis import given
import hypothesis.strategies as st

@given( st.lists(st.integers(), min_size=4, max_size=(4)))
def test_lenlist(len_list):
    output = SORT.sort_layers(len_list)
    assert len(output) == len(len_list)
    
    
@given( st.lists(st.integers(), min_size=5)  )
def test_longlist(t_list):
    output = SORT.sort_layers(t_list)
    assert output == ValueError
    
@given( st.lists(st.integers(), min_size=0, max_size=(3))  )
def test_shortlist(t_list):
    output = SORT.sort_layers(t_list)
    assert output == ValueError

@given( st.lists(st.integers(), min_size=4, max_size=(4)))
def test_sortedlist(srt_list):
    bx = [2, 5, 3, 7]
    output = SORT.sort_layers(bx)
    assert output == bx
    
@given( st.lists(st.integers(), min_size=4, max_size=(4)))
def test_sortlayers(bxlist):
    output = SORT.sort_layers(bxlist)
    L4= output[0]
    L3= output[2]
    L2= output[1]
    L1= output[3]
    assert L4 <= L3
    assert L3 <= L2
    assert L2 <= L1
    
