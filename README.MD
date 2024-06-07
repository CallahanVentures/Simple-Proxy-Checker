<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #0073e6;
        }
        code {
            background: #eaeaea;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background: #eaeaea;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Proxy Data Scraper</h1>
        <p>This simple script scrapes proxy data from Scamalytics and stores the results in a CSV file. It uses multiple threads for faster processing and random user agents to avoid being blocked by the target site.</p>
        
        <h2>Features</h2>
        <ul>
            <li>Scrapes detailed proxy information from Scamalytics</li>
            <li>Uses random user agents to avoid detection</li>
            <li>Multithreaded for faster processing</li>
            <li>Stores results in a CSV file</li>
        </ul>
        
        <h2>Requirements</h2>
        <p>Ensure you have the following Python libraries installed:</p>
        <ul>
            <li>requests</li>
            <li>beautifulsoup4</li>
            <li>random_user_agent</li>
        </ul>
        <pre><code>pip install requests beautifulsoup4 random_user_agent</code></pre>
        
        <h2>Usage</h2>
        <ol>
            <li>Place your list of proxies in a file named <code>proxies.txt</code> in the same directory as the script.</li>
            <li>Run the script.</li>
        </ol>
        <pre><code>python proxy_data_scraper.py</code></pre>
   >
    </div>
</body>
</html>
