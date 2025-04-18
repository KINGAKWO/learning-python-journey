def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    """
    Creates a sandwich description with optional cheese and toast.

    Args:
        bread_type (str): Type of bread (required)
        filling (str): Type of filling (required)
        cheese (str, optional): Type of cheese (optional)
        toasted (bool, optional): Whether it's toasted (default is False)

    Returns:
        str: A description of the sandwich
    """
    
    #  the string description
    description = ""

    if toasted:
        description += "Toasted sandwich with "
    else:
        description += "Sandwich with "

    description += f"{bread_type} bread, {filling} filling"

    if cheese:
        description += f", and {cheese} cheese"
    else:
        description += ", no cheese"

    description += "."

    return description
