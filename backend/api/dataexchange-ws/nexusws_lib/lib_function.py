

def modelToJson(modelObjs):
    all_data = []
    for modelObj in modelObjs:
        # modelObj.__dict__
        columns = []
        ret_data = {}
        try:
            columns =modelObj.__table__.columns.keys()
        except:
            continue
        for key in columns:
            ret_data[key] = getattr(modelObj, key)
        all_data.append(ret_data)
    all_jsn_data = {"data":all_data}
        
    return all_jsn_data