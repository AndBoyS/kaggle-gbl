def colab_setup_if_available():
    # check if in colab
    try:
        import google.colab
        in_colab = True
    except:
        in_colab = False

    if not in_colab:
        return

    #TODO access drive and install requirements
    raise NotImplementedError
