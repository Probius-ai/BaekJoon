import java.util.Arrays;

public class PCCP_1 {
    public String solution(String videoLen, String pos, String opStart, String opEnd, String[] commands) {
        String answer = "";
        
        // Convert time to seconds
        int secLen = convertToSeconds(videoLen);
        int secPos = convertToSeconds(pos);
        int secStart = convertToSeconds(opStart);
        int secEnd = convertToSeconds(opEnd);
        
        for (String command : commands) {
            // Skip opening
            if (secPos >= secStart && secPos <= secEnd) {
                secPos = secEnd;
            }
            
            if (command.equals("prev")) {
                secPos -= 10;
                if (secPos < 0) {
                    secPos = 0;
                }
            } else if (command.equals("next")) {
                secPos += 10;
                if (secPos > secLen) {
                    secPos = secLen;
                }
            }
            
            if (secPos >= secStart && secPos <= secEnd) {
                secPos = secEnd;
            }
        }
        
        answer = String.format("%02d:%02d", secPos / 60, secPos % 60);
        return answer;
    }
    
    private int convertToSeconds(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
    }
}