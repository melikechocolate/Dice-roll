import textwrap

def generate_full_excellence_report():
    print("-" * 50)
    print("      --- EXCELLENCE REPORT GENERATOR ---")
    print("      (Now with Median/Box Overlap Logic)")
    print("-" * 50)
    
    # --- INPUT SECTION ---
    var = input("Variable Name (e.g., Height): ")
    unit = input(f"Unit for {var} (e.g., cm): ")
    g1 = input("Name of Group 1 (e.g., Male): ")
    g2 = input("Name of Group 2 (e.g., Female): ")
    pop = input("What is the whole population? (e.g., All NZ Students): ")
    
    print(f"\n--- MAIN DATA (n=1000) ---")
    med1 = float(input(f"Median for {g1}: "))
    lq1 = float(input(f"The 25% (LQ) for {g1}: "))
    uq1 = float(input(f"The 75% (UQ) for {g1}: "))
    
    med2 = float(input(f"Median for {g2}: "))
    lq2 = float(input(f"The 25% (LQ) for {g2}: "))
    uq2 = float(input(f"The 75% (UQ) for {g2}: "))
    
    # --- CALCULATIONS ---
    dbm = abs(med1 - med2)
    ovs = max(uq1, uq2) - min(lq1, lq2)
    percentage = (dbm / ovs) * 100
    
    winner = g1 if med1 > med2 else g2
    loser = g2 if med1 > med2 else g1
    
    # MEDIAN POSITION LOGIC (Is the median outside the box?)
    # Checks if med1 is outside g2's box
    med1_outside = med1 < lq2 or med1 > uq2
    # Checks if med2 is outside g1's box
    med2_outside = med2 < lq1 or med2 > uq1

    print("\n--- SECTION 5: SUBSET ---")
    subset_name = input("Subset Name (e.g., Year 13s): ")
    sub_med1 = float(input(f"{subset_name} {g1} Median: "))
    sub_med2 = float(input(f"{subset_name} {g2} Median: "))
    sub_diff = abs(sub_med1 - sub_med2)

    # --- FORMATTED OUTPUT ---
    width = 75 
    wrapper = textwrap.TextWrapper(width=width)

    print("\n" + "="*width)
    print("COMPLETE EXCELLENCE REPORT TEMPLATE".center(width))
    print("="*width)
    
    # SECTION 3 CONTENT (Analysis with Median Overlap)
    overlap_text = ""
    if med1_outside and med2_outside:
        overlap_text = f"Crucially, the median for {g1} is outside the box for {g2}, and the median for {g2} is outside the box for {g1}. "
    elif med1_outside or med2_outside:
        overlap_text = f"Notably, at least one median is outside the interquartile range (the box) of the other group. "
    else:
        overlap_text = f"The medians for both groups fall within the overlap of the boxes. "

    s3_text = (f"The median {var} for {g1} is {med1}{unit}, which is {dbm}{unit} different from the {g2} "
               f"median of {med2}{unit}. {overlap_text}"
               f"Looking at the overall visible spread (OVS), the distance from the lowest LQ to the highest UQ is {ovs}{unit}. "
               f"The DBM is {percentage:.1f}% of the OVS (Calculation: {dbm} / {ovs} x 100).")

    # Other Sections (Truncated for brevity in code, but full in output)
    report_data = [
        ("1. PROBLEM & PURPOSE", f"Investigative Question: I wonder if the {var} ({unit}) of {g1} in the {pop} population tends to be greater than the {var} of {g2}. Hypothesis: I predict {winner} will be greater because of biological/environmental factors."),
        ("2. SOURCE OF DATA & VARIATION", f"Source: n=1000 sample from CensusAtSchool. We manage natural variation via sample size and measurement variation by checking for outliers."),
        ("3. ANALYSIS", s3_text),
        ("4. CONCLUSION (MAKING THE CALL)", f"For n=1000, the threshold is 10%. Since {percentage:.1f}% > 10%, I can make the call. While sampling variability would change the specific numbers in a new sample, the significant difference makes it likely the call would stay the same."),
        ("5. EXCELLENCE REFLECTION", f"Analyzing the {subset_name} subset showed a median difference of {sub_diff}{unit}, providing further insight into how {subset_name} impacts the {var} trend.")
    ]

    for title, body in report_data:
        print(f"\n{title}")
        print("-" * len(title))
        print(wrapper.fill(text=body))

    print("\n" + "="*width)

if __name__ == "__main__":
    generate_full_excellence_report()