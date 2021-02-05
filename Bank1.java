package com.inherit;

import java.util.Scanner;

class Accounts {
	float currentamount = 10000;
	float depamount;
	float withdraw;
	float depbalance;
	final float minbal = 100;

	public void deposit() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the amount to be deposited:");
		depamount = sc.nextFloat();
		depbalance = currentamount + depamount;
		currentamount = depbalance;
		System.out.println("The acc balance after deposit " + depbalance);
	}

	public void withdraw() {
		Scanner sc1 = new Scanner(System.in);
		do {
			System.out.println("Enter the amount to be withdrawn in multiples of 100:");
			withdraw = sc1.nextFloat();
		} while (withdraw < minbal);
	}
}

class Savings extends Accounts {
	float balance;
	public void saving() {
		balance = currentamount - withdraw;
		if (balance <= 100) {
			System.out.println("You cant withdraw the amount, your balance is low!");
		}
	}
}

class CheckBal extends Savings {
	public void ck_bal() {
		System.out.println("The balance of your account is : " + balance);
	}
}

public class Bank {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CheckBal obj = new CheckBal();
		obj.deposit();
		obj.withdraw();
		obj.saving();
		obj.ck_bal();
	}
}
