def isCorrectRect(rect):
    if rect[0][0] < rect[1][0] and rect[0][1] < rect[1][1]:
        return True
    else:
        return False