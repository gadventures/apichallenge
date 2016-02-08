package annakovale.trips;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        new RetrieveFeedTask().execute();
    }
    
    class RetrieveFeedTask extends AsyncTask<Void, Void, String> {

        private Exception exception;

        /*** Requests content from the API ***/
        protected String doInBackground(Void... urls) {

            try {
                // API has no key, simple URL is enough
                URL url = new URL("http://10.0.2.2:8000/trips/api/");
                // Sets up a connection, parses content into String
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                try {
                    BufferedReader bufferedReader =
                            new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = bufferedReader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    bufferedReader.close();
                    return stringBuilder.toString();
                }
                finally{
                    urlConnection.disconnect();
                }
            }
            catch(Exception e) {
                Log.e("ERROR", e.getMessage(), e);
                return null;
            }
        }

        protected void onPostExecute(String response) {
            if (response == null) {
                response = "THERE WAS AN ERROR";
            }
            /* Array associated with the listView object */
            ArrayList<String> data = new ArrayList<String>();
            // Header for the listView
            data.add("Trips | Start Date | Finish Date");
            ListView trips = (ListView) findViewById(R.id.tripList);
            // Binds the adapter to the listView
            ArrayAdapter<String> adapter =
                    new ArrayAdapter<String>(MainActivity.this,
                                            android.R.layout.simple_list_item_1,
                                            data);
            trips.setAdapter(adapter);

            // Parses JSON and populates the listView - one element at a time
            try {

                JSONArray jsonArray = new JSONArray(response);

                for (int i = 0; i < jsonArray.length(); i++) {
                    JSONObject jsonObject = jsonArray.getJSONObject(i);

                    adapter.add(jsonObject.optString("name").toString() + ".\nBegins on: " +
                                jsonObject.optString("start_date").toString() + ".\nEnds on " +
                                jsonObject.optString("finish_date").toString() + ".");
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    }
}


