//
//  TheImageView.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 26/05/2023.
//

import SwiftUI

struct TheImageView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        AsyncImage(url: URL(string: "\(textData.image_name!)")) { phase in
            if let image = phase.image {
                if textData.scall_to_fit == true {
                    image
                        .resizable()
                        .scaledToFit()
                        .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
                }else {
                    image
                        .resizable()
                        .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
                }
            } else if phase.error != nil {
                Text("Error while load the image!")
                    .background(.red)
                    .foregroundColor(.white)
                    .font(.title3)
            } else {
                
            }
        }
    }
}
