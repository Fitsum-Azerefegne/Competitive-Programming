class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0  
        for number_of_boxes, units_per_box in boxTypes:
            if truckSize == 0:
                break  # Stop when truck is full
          
            boxes_to_load = min(number_of_boxes, truckSize) # calc num of boxes to add it
            total_units += boxes_to_load * units_per_box 
            truckSize -= boxes_to_load 
        
        return total_units