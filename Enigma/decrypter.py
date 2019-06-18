def invertedDict():
    import plugboard
    invert = plugboard.getPlugboard()
    inv_dict = {v: k for k, v in invert.items()}
    return inv_dict
