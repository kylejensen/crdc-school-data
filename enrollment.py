if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    
    total_m = (data["TOT_ENR_M"].sum()/all_enrollment) * 100
    total_f = (data["TOT_ENR_F"].sum()/all_enrollment) * 100
    total_hi = ((data["SCH_ENR_HI_M"].sum() + data["SCH_ENR_HI_F"].sum())/all_enrollment) * 100
    total_am = ((data["SCH_ENR_AM_M"].sum() + data["SCH_ENR_AM_F"].sum())/all_enrollment) * 100
    total_as = ((data["SCH_ENR_AS_M"].sum() + data["SCH_ENR_AS_F"].sum())/all_enrollment) * 100
    total_hp = ((data["SCH_ENR_HP_M"].sum() + data["SCH_ENR_HP_F"].sum())/all_enrollment) * 100
    total_bl = ((data["SCH_ENR_BL_M"].sum() + data["SCH_ENR_BL_F"].sum())/all_enrollment) * 100
    total_wh = ((data["SCH_ENR_WH_M"].sum() + data["SCH_ENR_WH_F"].sum())/all_enrollment) * 100
    total_tr = ((data["SCH_ENR_TR_M"].sum() + data["SCH_ENR_TR_F"].sum())/all_enrollment) * 100
    
    races={
        "Female": total_f,
        "Male": total_m,
        "Hispanic": total_hi,
        "American Indian": total_am,
        "Asian": total_as,
        "Hawaiian or Pacific Islander": total_hp,
        "Black": total_bl,
        "White": total_wh,
        "Two or more races": total_tr
    }
    
    for key, val in races.items():
        print("The ratio of {} pop is {}".format(key, val))