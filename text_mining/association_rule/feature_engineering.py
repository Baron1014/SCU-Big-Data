import config as cg

def feature_engineering(var):
    rr=list()
    for i in var:
        for j in i:
            if j in cg.constellationlist:
                if j in cg.tidy:
                    i.remove(j)
                    i.append(cg.tidy[1])
                elif j in cg.clever:
                    i.remove(j)
                    i.append(cg.clever[1])
                elif j in cg.romantic:
                    i.remove(j)
                    i.append(cg.romantic[1])
                elif j in cg.generous:
                    i.remove(j)
                    i.append(cg.generous[1])
                elif j in cg.reliable:
                    i.remove(j)
                    i.append(cg.reliable[1])
                elif j in cg.witty:
                    i.remove(j)
                    i.append(cg.witty[1])
                elif j in cg.frugal:
                    i.remove(j)
                    i.append(cg.frugal[1])
                elif j in cg.lion:
                    i.remove(j)
                    i.append(cg.lion[1])
                elif j in cg.passionate:
                    i.remove(j)
                    i.append(cg.passionate[1])
                elif j in cg.optimistic:
                    i.remove(j)
                    i.append(cg.optimistic[2])
                elif j in cg.calm:
                    i.remove(j)
                    i.append(cg.calm[1])
                elif j in cg.diplomatic:
                    i.remove(j)
                    i.append(cg.diplomatic[1])
        rr.append(i)