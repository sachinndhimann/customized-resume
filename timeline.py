import preprocess

data_list=[]



    
for value in preprocess.timeline_info:
    title=value[0].strip()
    div=f"""<div class="timeline">
    <div class="timeline-item">
      <div class="timeline-content"> 
        <div class="timeline-company">{title}</div>
        <div class="timeline-description">
          {value[1]}</div>
      </div>
    </div>"""
    data_list.append(div)




html="""<!DOCTYPE html>
<html>
<head>
  <title>Work Experience Timeline</title>
  <style>
      body {
      font-family: Arial, sans-serif;
      background-color: #f8f8f8;
    }
    
    .timeline {
      position: relative;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .timeline-item {
      position: relative;
      margin-bottom: 50px;
    }
    
    .timeline-item:last-child {
      margin-bottom: 0;
    }
    
    .timeline-content {
      position: relative;
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      overflow-y: auto; /* Add scroll bar for overflow */
      max-height: 200px; /* Adjust the max height as needed */
      white-space: pre-wrap;
    }
    
    .timeline-date {
      font-weight: bold;
      font-size: 1.2em;
      margin-bottom: 10px;
      color: #333;
      white-space: pre-wrap;
    }
    
    .timeline-company {
      font-weight: bold;
      margin-bottom: 5px;
      color: #555;
      white-space: pre-wrap;
    }
    
    .timeline-job-title {
      font-style: italic;
      margin-bottom: 10px;
      color: #777;
      white-space: pre-wrap;
    }
    
    .timeline-description {
      margin-bottom: 20px;
      color: #333;
      white-space: pre-wrap;
    }
  </style>
</head>
<body> <div class="timeline">"""+"\n".join(data_list)+""" </div>
</body>
</html>
"""
