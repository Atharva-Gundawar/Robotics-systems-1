% Ask the user for the letter
letter = input('Enter the letter (A-Z): ', 's');

% Check if the input is a capital letter
if ~isletter(letter) || length(letter) ~= 1 || letter < 'A' || letter > 'Z'
    disp('Invalid input. Please enter a capital letter (A-Z).');
    return;
end

% Load the line segment data for the selected letter
filename = ['ls_', letter, '.txt'];
fid = fopen(filename, 'r');

if fid == -1
    disp(['Line segment data for letter ', letter, ' not found.']);
    return;
end

lineData = textscan(fid, '%d,%d,%d,%d', 'Delimiter', '\n');
fclose(fid);

% Assuming MyCobot is already initialized and connected, you can now send
% the line segments for tracing
for i = 1:length(lineData{1})
    x1 = lineData{1}(i);
    y1 = lineData{2}(i);
    x2 = lineData{3}(i);
    y2 = lineData{4}(i);
    
    % Send the line segment coordinates to MyCobot for tracing
    % Replace the following lines with MyCobot SDK commands for movement
    % e.g., MyCobot.moveLinear([x1, y1, z1], [x2, y2, z2], speed);
    
    disp(['Tracing line segment ', num2str(i), ':']);
    disp(['Start: (', num2str(x1), ', ', num2str(y1), ')']);
    disp(['End:   (', num2str(x2), ', ', num2str(y2), ')']);
    % Pause for a moment to simulate MyCobot's movement
    pause(1); % Adjust the pause time as needed
end

% Close the connection to MyCobot if needed
% e.g., MyCobot.disconnect();
