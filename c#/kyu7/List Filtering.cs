using System.Collections.Generic;

public static class ListFilterer
{
    public static List<int> GetIntegersFromList(List<object> listOfItems)
    {
        List<int> integersList = new List<int>();

        foreach (object item in listOfItems)
        {
            if (item is int && (int)item >= 0)
            {
                integersList.Add((int)item);
            }
        }

        return integersList;
    }
}
