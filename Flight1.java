
public class Flight {
	
	String flight_name, destination,origin;
	int flight_num;
	
	
	public Flight(String flight_name, String destination, String origin, int flight_num)
	{
		this.flight_name = flight_name;
		this.flight_num = flight_num;
		this.destination = destination;
		this.origin = origin;
		
		
		
	}
	public void set_Name(String flight_name)
	{
		this.flight_name = flight_name;
	}
	
	public String get_Name()
	{
		return flight_name;
	}
	
	public void set_flightNum(int flight_num )
	{
		 this.flight_num = flight_num;
	}
	
	public int get_flightNum()
	{
		return flight_num;
	}
	
	public void set_Destination(String destination)
	{
		this.destination = destination;
	}
	
	public String get_Destination()
	{
		return destination;
	}
	
	public void set_Origin(String origin)
	{
		this.origin = origin;
	}
	
	public String get_Origin()
	{
		return origin;
	}
	
	
	public String toString()
	{
		return "Flight name is "+get_Name()+" "+get_flightNum()+" Departing from " +get_Origin()+ " and Destination: "+get_Destination() ;
	}
	


}
