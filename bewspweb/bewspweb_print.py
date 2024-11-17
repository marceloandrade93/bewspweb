def bewspweb_print(list=None, col_a=0, col_b=1):
    """
    Objective:
    This function is to print the collected data from a web page.

    Args:
        list (list): List with the data collected. Defaults to None.
        col_a (int): Column A. Defaults to 0.
        col_b (int): Column B. Defaults to 1.
    """

    for i in list:
        print(f"{i[col_a]} | {i[col_b]}")
