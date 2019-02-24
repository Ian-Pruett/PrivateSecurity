package com.example.ethicalskynetapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button signIn, createAccount;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        signIn = (Button)findViewById(R.id.SignIn);
        createAccount = (Button)findViewById(R.id.Create);

        signIn.setOnClickListener(this);
        createAccount.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId())
        {
            case R.id.SignIn:
                startActivity(new Intent(this,Login.class));
                break;

            case  R.id.Create:
                startActivity(new Intent(this,Register.class));

        }
    }
}
